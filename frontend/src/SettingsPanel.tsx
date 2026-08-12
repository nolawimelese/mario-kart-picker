import { Dialog, Switch, useTheme } from "./design-system";

export interface SettingsPanelProps {
  open: boolean;
  onClose: () => void;
}

/** Settings dialog, opened from the TopNav gear icon. */
export function SettingsPanel({ open, onClose }: SettingsPanelProps) {
  const { darkMode, setDarkMode } = useTheme();

  return (
    <Dialog open={open} onClose={onClose} title="Settings" icon="settings">
      <Switch checked={darkMode} onChange={setDarkMode} label="Dark mode" />
    </Dialog>
  );
}
