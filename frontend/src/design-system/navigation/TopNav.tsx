import React from "react";
import { Logo } from "../brand/Logo";
import { IconButton } from "../core/IconButton";
import { Tabs } from "./Tabs";
import type { TabItem } from "./Tabs";

export interface TopNavProps extends Omit<React.HTMLAttributes<HTMLElement>, "onChange"> {
  tabs?: TabItem[];
  value?: string;
  defaultValue?: string;
  onChange?: (value: string) => void;
}

const defaultTabs: TabItem[] = [
  { value: "course-picker", label: "Course Picker", icon: "map" },
  { value: "browse", label: "Browse", icon: "search" },
];

/**
 * MK Picker top navigation bar — logo lockup on the left, section tabs on
 * the right, chunky ink border underneath to match the arcade aesthetic.
 */
export function TopNav({
  tabs = defaultTabs,
  value,
  defaultValue,
  onChange,
  style,
  ...rest
}: TopNavProps) {
  return (
    <header
      style={{
        display: "flex",
        alignItems: "center",
        gap: 24,
        padding: "14px 32px",
        background: "var(--cream)",
        borderBottom: "var(--border-base) solid var(--ink-900)",
        ...style,
      }}
      {...rest}
    >
      <Logo variant="full" size={30} />
      <Tabs tabs={tabs} value={value} defaultValue={defaultValue ?? tabs[0]?.value} onChange={onChange} />
      <IconButton icon="settings" variant="ghost" label="Settings" style={{ marginLeft: "auto" }} />
    </header>
  );
}
