import React from "react";
import { Icon } from "../brand/Icon";

export interface SelectOption { value: string; label: string; }

export interface SelectProps extends Omit<React.SelectHTMLAttributes<HTMLSelectElement>, "size"> {
  /** Option list — strings or {value,label}. */
  options?: (string | SelectOption)[];
  size?: "sm" | "md" | "lg";
}

/** Native select styled as an MK Picker control, with a chevron affordance. */
export function Select({ options = [], size = "md", style, ...rest }: SelectProps) {
  const heights = { sm: "var(--control-h-sm)", md: "var(--control-h-md)", lg: "var(--control-h-lg)" };
  const [focused, setFocused] = React.useState(false);
  return (
    <div
      style={{
        position: "relative",
        display: "inline-flex",
        alignItems: "center",
        height: heights[size] || heights.md,
      }}
    >
      <select
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
        {...rest}
        style={{
          appearance: "none",
          WebkitAppearance: "none",
          height: "100%",
          width: "100%",
          padding: "0 38px 0 14px",
          fontFamily: "var(--font-ui)",
          fontWeight: "var(--weight-medium)",
          fontSize: "var(--text-md)",
          color: "var(--ink-900)",
          background: "var(--white)",
          border: `var(--border-base) solid ${focused ? "var(--boost-500)" : "var(--ink-200)"}`,
          borderRadius: "var(--radius-sm)",
          boxShadow: focused ? "0 0 0 3px var(--boost-100)" : "none",
          cursor: "pointer",
          outline: "none",
          ...style,
        }}
      >
        {options.map((o) => {
          const val = typeof o === "string" ? o : o.value;
          const label = typeof o === "string" ? o : o.label;
          return <option key={val} value={val}>{label}</option>;
        })}
      </select>
      <span style={{ position: "absolute", right: 12, pointerEvents: "none", display: "grid" }}>
        <Icon name="chevron-down" size={18} color="var(--ink-500)" />
      </span>
    </div>
  );
}
