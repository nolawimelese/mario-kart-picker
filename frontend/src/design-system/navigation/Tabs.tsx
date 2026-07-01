import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface TabItem {
  value: string;
  label: string;
  icon?: IconName;
  /** Optional count pill. */
  count?: number;
}

export interface TabsProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "onChange"> {
  tabs: TabItem[];
  value?: string;
  defaultValue?: string;
  onChange?: (value: string) => void;
}

/**
 * Tabs — pill-style segmented nav. Active tab gets the boost pop treatment.
 * Controlled via `value` + `onChange`, or uncontrolled with `defaultValue`.
 */
export function Tabs({ tabs = [], value, defaultValue, onChange, style, ...rest }: TabsProps) {
  const [internal, setInternal] = React.useState(defaultValue ?? (tabs[0] && tabs[0].value));
  const active = value !== undefined ? value : internal;
  const select = (v: string) => { setInternal(v); onChange && onChange(v); };

  return (
    <div
      style={{
        display: "inline-flex",
        gap: 4,
        padding: 4,
        background: "var(--ink-100)",
        border: "var(--border-base) solid var(--ink-200)",
        borderRadius: "var(--radius-pill)",
        ...style,
      }}
      {...rest}
    >
      {tabs.map((t) => {
        const isActive = t.value === active;
        return (
          <button
            key={t.value}
            type="button"
            onClick={() => select(t.value)}
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: 7,
              height: 36,
              padding: "0 16px",
              border: isActive ? "var(--border-base) solid var(--ink-900)" : "var(--border-base) solid transparent",
              borderRadius: "var(--radius-pill)",
              background: isActive ? "var(--boost-500)" : "transparent",
              color: isActive ? "#fff" : "var(--ink-600)",
              fontFamily: "var(--font-ui)",
              fontWeight: "var(--weight-semibold)",
              fontSize: "var(--text-sm)",
              cursor: "pointer",
              boxShadow: isActive ? "var(--shadow-pop-sm)" : "none",
              transition: "background var(--dur-fast), color var(--dur-fast)",
              whiteSpace: "nowrap",
            }}
          >
            {t.icon && <Icon name={t.icon} size={16} />}
            {t.label}
            {t.count != null && (
              <span style={{
                fontFamily: "var(--font-mono)",
                fontSize: "var(--text-xs)",
                padding: "1px 6px",
                borderRadius: 999,
                background: isActive ? "rgba(255,255,255,0.25)" : "var(--ink-200)",
                color: isActive ? "#fff" : "var(--ink-600)",
              }}>{t.count}</span>
            )}
          </button>
        );
      })}
    </div>
  );
}
