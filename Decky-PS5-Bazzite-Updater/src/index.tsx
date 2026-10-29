import {
  ButtonItem,
  ConfirmModal,
  DialogButton,
  Focusable,
  ModalRoot,
  Navigation,
  PanelSection,
  PanelSectionRow,
  showModal,
  staticClasses,
} from "@decky/ui";
import { addEventListener, callable, definePlugin, removeEventListener, toaster } from "@decky/api";
import { useEffect, useState } from "react";
import { FaSyncAlt } from "react-icons/fa";
import { t } from "./i18n";

type Release = { tag: string; name: string; published: string | null; body: string; url: string; prerelease: boolean };
type Status = { installed: string; stable?: Release | null; pre?: Release | null; error?: string };
type UpdateResult = { ok: boolean; error?: string; log?: string; undo?: string };

const getStatus = callable<[], Status>("get_status");
const runUpdate = callable<[tag: string], UpdateResult>("update");
const powerOff = callable<[], void>("poweroff");

const CHECK_EVERY_MS = 6 * 60 * 60 * 1000;
const POWEROFF_DELAY_S = 10;

// Module-level state so an update keeps going (and stays visible) when the menu is closed
type State = {
  status?: Status; checkedAt?: Date; checking: boolean;
  updating?: string; log: string[]; result?: UpdateResult; countdown?: number;
};
let state: State = { checking: false, log: [] };
const subs = new Set<() => void>();
const set = (patch: Partial<State>) => { state = { ...state, ...patch }; subs.forEach((f) => f()); };
function useStore() {
  const [, force] = useState(0);
  useEffect(() => { const f = () => force((n) => n + 1); subs.add(f); return () => { subs.delete(f); }; }, []);
  return state;
}

async function check(notify: boolean) {
  set({ checking: true });
  const status = await getStatus().catch(() => ({ installed: "?", error: t("Backend error") }) as Status);
  set({ status, checkedAt: new Date(), checking: false });
  const newest = status.pre ?? status.stable;
  if (notify && newest && newest.tag !== status.installed) {
    let seen: string | null = null;
    try { seen = localStorage.getItem("ps5-updates-notified"); } catch {}
    if (seen !== newest.tag) {
      toaster.toast({ title: t("PS5 Updates"), body: t("{{tag}} available{{prerelease}}", { tag: newest.tag, prerelease: newest.prerelease ? t(" (pre-release)") : "" }) });
      try { localStorage.setItem("ps5-updates-notified", newest.tag); } catch {}
    }
  }
}

let timer: ReturnType<typeof setInterval> | undefined;
function cancelPowerOff() { if (timer) clearInterval(timer); timer = undefined; set({ countdown: undefined }); }

async function startUpdate(r: Release) {
  set({ updating: r.tag, log: [], result: undefined });
  const result = await runUpdate(r.tag).catch((e) => ({ ok: false, error: String(e) }));
  set({ updating: undefined, result });
  if (!result.ok) {
    toaster.toast({ title: t("PS5 Updates"), body: t("Update failed: {{error}}", { error: result.error ?? "" }) });
    return;
  }
  toaster.toast({ title: t("PS5 Updates"), body: t("{{tag}} installed. Powering off in {{seconds}} s", { tag: r.tag, seconds: POWEROFF_DELAY_S }) });
  set({ countdown: POWEROFF_DELAY_S });
  timer = setInterval(() => {
    const left = (state.countdown ?? 0) - 1;
    if (left > 0) return set({ countdown: left });
    cancelPowerOff();
    powerOff();
  }, 1000);
}

function confirmUpdate(r: Release) {
  showModal(
    <ConfirmModal
      strTitle={t("Update to {{tag}}?", { tag: r.tag })}
      strDescription={
        t("Installs the new kernel (with a backup) and powers off the PS5. Then turn it on and start Linux with the loader.") +
        (r.prerelease ? t(" This is a pre-release (test build).") : "")
      }
      strOKButtonText={t("Continue")}
      strCancelButtonText={t("Cancel")}
      onOK={() => startUpdate(r)}
    />,
  );
}

// Minimal markdown: headings, bullets, and stripped emphasis/links
function Notes({ body }: { body: string }) {
  const clean = (s: string) => s.replace(/\*\*(.+?)\*\*/g, "$1").replace(/`([^`]+)`/g, "$1").replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");
  const lines = body.replace(/\r/g, "").split("\n").filter((l) => !/^```/.test(l));
  return (
    <div style={{ fontSize: "14px", lineHeight: 1.5 }}>
      {lines.map((l, i) => {
        if (/^#+\s/.test(l)) return <div key={i} style={{ fontWeight: "bold", marginTop: "12px" }}>{clean(l.replace(/^#+\s/, ""))}</div>;
        if (/^\s*[-*]\s/.test(l)) return <div key={i} style={{ paddingLeft: "14px", textIndent: "-10px" }}>• {clean(l.replace(/^\s*[-*]\s/, ""))}</div>;
        if (!l.trim()) return <div key={i} style={{ height: "6px" }} />;
        return <div key={i}>{clean(l)}</div>;
      })}
    </div>
  );
}

function showNotes(r: Release, installed: string) {
  const modal = showModal(
    <ModalRoot onCancel={() => modal.Close()}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div style={{ fontSize: "20px", fontWeight: "bold" }}>{r.name}</div>
        <Badge pre={r.prerelease} />
      </div>
      <div style={{ opacity: 0.7, marginBottom: "8px" }}>{ago(r.published)} · {t("Installed:")} {installed}</div>
      <div style={{ maxHeight: "55vh", overflowY: "auto" }}><Notes body={r.body} /></div>
      <Focusable style={{ display: "flex", gap: "8px", marginTop: "16px" }}>
        <DialogButton onClick={() => modal.Close()}>{t("Close")}</DialogButton>
        <DialogButton onClick={() => { modal.Close(); Navigation.NavigateToExternalWeb(r.url); }}>{t("Open on GitHub")}</DialogButton>
        {r.tag !== installed && (
          <DialogButton onClick={() => { modal.Close(); confirmUpdate(r); }}>{t("Update and power off")}</DialogButton>
        )}
      </Focusable>
    </ModalRoot>,
  );
}

function ago(iso: string | null) {
  if (!iso) return "";
  const h = Math.round((Date.now() - new Date(iso).getTime()) / 3.6e6);
  return h < 1 ? t("just now") : h < 48 ? t("{{hours}} h ago", { hours: h }) : t("{{days}} days ago", { days: Math.round(h / 24) });
}

function Badge({ pre }: { pre: boolean }) {
  return (
    <span style={{
      fontSize: "11px", padding: "1px 8px", borderRadius: "4px",
      background: pre ? "rgba(239,159,39,0.25)" : "rgba(99,153,34,0.3)", color: pre ? "#FAC775" : "#C0DD97",
    }}>{pre ? t("Pre-release") : t("Stable")}</span>
  );
}

function ReleaseCard({ r, installed }: { r: Release; installed: string }) {
  const current = r.tag === installed;
  return (
    <PanelSectionRow>
      <div style={{
        border: `1px solid ${r.prerelease ? "rgba(239,159,39,0.6)" : "rgba(255,255,255,0.15)"}`,
        borderRadius: "6px", padding: "8px", marginBottom: "4px",
      }}>
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <b>{r.tag}</b><Badge pre={r.prerelease} />
        </div>
        <div style={{ opacity: 0.7, fontSize: "12px" }}>{current ? t("Up to date") : `${ago(r.published)} · ${r.name.replace(/^v[\d.]+\s*[–-]\s*/, "")}`}</div>
      </div>
      <ButtonItem layout="below" onClick={() => showNotes(r, installed)}>{t("Release notes")}</ButtonItem>
      {!current && <ButtonItem layout="below" disabled={!!state.updating} onClick={() => confirmUpdate(r)}>{t("Install and power off")}</ButtonItem>}
    </PanelSectionRow>
  );
}

function Content() {
  const s = useStore();
  const st = s.status;

  if (s.updating || s.countdown !== undefined || s.result) {
    return (
      <PanelSection title={s.updating ? t("Updating to {{tag}}", { tag: s.updating }) : t("Update")}>
        <PanelSectionRow>
          <div style={{ fontSize: "11px", fontFamily: "monospace", whiteSpace: "pre-wrap", maxHeight: "240px", overflowY: "auto" }}>
            {(s.result && !s.result.ok ? (s.result.log ?? "") : s.log.slice(-12).join("\n"))}
          </div>
        </PanelSectionRow>
        {s.result && !s.result.ok && (
          <PanelSectionRow><div style={{ color: "#F09595" }}>{s.result.error} {t("The PS5 stays on.")}</div></PanelSectionRow>
        )}
        {s.countdown !== undefined && (
          <PanelSectionRow>
            <ButtonItem layout="below" onClick={cancelPowerOff}>{t("Cancel power off ({{seconds}} s)", { seconds: s.countdown })}</ButtonItem>
          </PanelSectionRow>
        )}
        {s.result && s.countdown === undefined && (
          <PanelSectionRow>
            <ButtonItem layout="below" onClick={() => { set({ result: undefined }); check(false); }}>{t("Back")}</ButtonItem>
          </PanelSectionRow>
        )}
      </PanelSection>
    );
  }

  return (
    <PanelSection>
      <PanelSectionRow>
        <div style={{ opacity: 0.8 }}>{t("Installed:")} <b>{st?.installed ?? "…"}</b></div>
      </PanelSectionRow>
      {st?.error && <PanelSectionRow><div style={{ color: "#F09595" }}>{st.error}</div></PanelSectionRow>}
      {st?.stable && <ReleaseCard r={st.stable} installed={st.installed} />}
      {st?.pre && <ReleaseCard r={st.pre} installed={st.installed} />}
      <PanelSectionRow>
        <ButtonItem layout="below" disabled={s.checking} onClick={() => check(false)}>
          {s.checking ? t("Checking…") : t("Check now")}
        </ButtonItem>
      </PanelSectionRow>
      {s.checkedAt && (
        <PanelSectionRow>
          <div style={{ opacity: 0.6, fontSize: "11px" }}>{t("Checked at {{time}}", { time: s.checkedAt.toLocaleTimeString().slice(0, 5) })}</div>
        </PanelSectionRow>
      )}
    </PanelSection>
  );
}

export default definePlugin(() => {
  const listener = addEventListener<[line: string]>("update_log", (line) => set({ log: [...state.log, line] }));
  check(true);
  const interval = setInterval(() => check(true), CHECK_EVERY_MS);

  return {
    name: t("PS5 Updates"),
    titleView: <div className={staticClasses.Title}>{t("PS5 Updates")}</div>,
    content: <Content />,
    icon: <FaSyncAlt />,
    onDismount() {
      removeEventListener("update_log", listener);
      clearInterval(interval);
      cancelPowerOff();
    },
  };
});
