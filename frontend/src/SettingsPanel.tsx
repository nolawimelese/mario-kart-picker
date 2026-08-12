import { Dialog, Tabs, useTheme } from "./design-system";
import type { ThemePreference } from "./design-system";

export interface SettingsPanelProps {
  open: boolean;
  onClose: () => void;
}

const VISUAL_OPTIONS = [
  { value: "light", label: "Light" },
  { value: "dark", label: "Dark" },
  { value: "system", label: "Auto" },
];

/** Settings dialog, opened from the TopNav gear icon. */
export function SettingsPanel({ open, onClose }: SettingsPanelProps) {
  const { preference, setPreference } = useTheme();

  return (
    <Dialog open={open} onClose={onClose} title="Settings" icon="settings">
      {/* Not a <label>: Tabs renders buttons, so the group is named via aria-label instead. */}
      <div
        style={{
          marginBottom: 8,
          fontSize: "var(--text-md)",
          fontWeight: "var(--weight-semibold)",
          color: "var(--text-strong)",
        }}
      >
        Visuals
      </div>
      <Tabs
        tabs={VISUAL_OPTIONS}
        value={preference}
        onChange={(next) => setPreference(next as ThemePreference)}
        role="group"
        aria-label="Visuals"
      />
      <p
        style={{
          margin: "8px 0 0",
          fontSize: "var(--text-sm)",
          fontWeight: 600,
          color: "var(--text-muted)",
        }}
      ></p>
    </Dialog>
  );
}
