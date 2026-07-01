import React from "react";
import { Icon } from "../brand/Icon";
import type { IconName } from "../brand/Icon";

export interface InputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "size"> {
  /** Leading icon name. */
  icon?: IconName;
  size?: "sm" | "md" | "lg";
  /** Red error state. */
  invalid?: boolean;
  /** Style overrides for the wrapper element. */
  wrapStyle?: React.CSSProperties;
}

/** Text input with optional leading icon. Rounded, ink-bordered, boost focus. */
export function Input({ icon, size = "md", invalid = false, style, wrapStyle, ...rest }: InputProps) {
  const heights = { sm: "var(--control-h-sm)", md: "var(--control-h-md)", lg: "var(--control-h-lg)" };
  const [focused, setFocused] = React.useState(false);
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        gap: 8,
        height: heights[size] || heights.md,
        padding: icon ? "0 14px 0 12px" : "0 14px",
        background: "var(--white)",
        border: `var(--border-base) solid ${invalid ? "var(--shell-red)" : focused ? "var(--boost-500)" : "var(--ink-200)"}`,
        borderRadius: "var(--radius-sm)",
        boxShadow: focused ? "0 0 0 3px var(--boost-100)" : "none",
        transition: "border-color var(--dur-fast), box-shadow var(--dur-fast)",
        ...wrapStyle,
      }}
    >
      {icon && <Icon name={icon} size={18} color="var(--ink-400)" />}
      <input
        onFocus={(e) => { setFocused(true); rest.onFocus && rest.onFocus(e); }}
        onBlur={(e) => { setFocused(false); rest.onBlur && rest.onBlur(e); }}
        {...rest}
        style={{
          flex: 1,
          minWidth: 0,
          border: "none",
          outline: "none",
          background: "transparent",
          fontFamily: "var(--font-body)",
          fontSize: "var(--text-md)",
          fontWeight: "var(--weight-semibold)",
          color: "var(--ink-900)",
          ...style,
        }}
      />
    </div>
  );
}
