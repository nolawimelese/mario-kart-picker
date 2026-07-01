import React from "react";

export interface SwitchProps {
  checked?: boolean;
  onChange?: (next: boolean) => void;
  label?: React.ReactNode;
  disabled?: boolean;
  style?: React.CSSProperties;
}

/** Toggle switch. Thumb has an ink outline; track turns boost when on. */
export function Switch({ checked = false, onChange, label, disabled = false, style, ...rest }: SwitchProps) {
  const sw = (
    <span
      onClick={() => !disabled && onChange && onChange(!checked)}
      style={{
        position: "relative",
        display: "inline-block",
        width: 48,
        height: 28,
        borderRadius: "var(--radius-pill)",
        background: checked ? "var(--boost-500)" : "var(--ink-300)",
        border: "var(--border-base) solid var(--ink-900)",
        cursor: disabled ? "not-allowed" : "pointer",
        transition: "background var(--dur-base) var(--ease-out)",
        flexShrink: 0,
      }}
    >
      <span
        style={{
          position: "absolute",
          top: 2,
          left: checked ? 22 : 2,
          width: 20,
          height: 20,
          borderRadius: "var(--radius-pill)",
          background: "#fff",
          border: "var(--border-base) solid var(--ink-900)",
          transition: "left var(--dur-base) var(--ease-snap)",
        }}
      />
    </span>
  );
  if (!label) return <span style={{ opacity: disabled ? 0.5 : 1, ...style }} {...rest}>{sw}</span>;
  return (
    <label
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 10,
        cursor: disabled ? "not-allowed" : "pointer",
        opacity: disabled ? 0.5 : 1,
        fontFamily: "var(--font-body)",
        fontWeight: "var(--weight-semibold)",
        fontSize: "var(--text-md)",
        color: "var(--ink-800)",
        userSelect: "none",
        ...style,
      }}
      {...rest}
    >
      {sw}
      {label}
    </label>
  );
}
