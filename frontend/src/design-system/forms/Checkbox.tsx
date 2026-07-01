import React from "react";
import { Icon } from "../brand/Icon";

export interface CheckboxProps {
  checked?: boolean;
  onChange?: (next: boolean) => void;
  label?: React.ReactNode;
  disabled?: boolean;
  style?: React.CSSProperties;
}

/** Checkbox with chunky ink outline; checks fill boost. */
export function Checkbox({ checked = false, onChange, label, disabled = false, style, ...rest }: CheckboxProps) {
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
      <span
        onClick={() => !disabled && onChange && onChange(!checked)}
        style={{
          display: "inline-grid",
          placeItems: "center",
          width: 24,
          height: 24,
          borderRadius: "var(--radius-xs)",
          background: checked ? "var(--boost-500)" : "var(--white)",
          border: "var(--border-base) solid var(--ink-900)",
          boxShadow: "var(--shadow-pop-sm)",
          transition: "background var(--dur-fast)",
        }}
      >
        {checked && <Icon name="check" size={16} color="#fff" strokeWidth={3} />}
      </span>
      {label}
    </label>
  );
}
