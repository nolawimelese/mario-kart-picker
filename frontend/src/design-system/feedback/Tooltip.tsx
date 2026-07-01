import React from "react";

export interface TooltipProps extends React.HTMLAttributes<HTMLSpanElement> {
  label: React.ReactNode;
  side?: "top" | "bottom" | "left" | "right";
  children: React.ReactNode;
}

/** Tooltip — hover bubble with an ink outline. Wraps any trigger element. */
export function Tooltip({ label, side = "top", children, style, ...rest }: TooltipProps) {
  const [show, setShow] = React.useState(false);
  const pos = {
    top: { bottom: "calc(100% + 8px)", left: "50%", transform: "translateX(-50%)" },
    bottom: { top: "calc(100% + 8px)", left: "50%", transform: "translateX(-50%)" },
    left: { right: "calc(100% + 8px)", top: "50%", transform: "translateY(-50%)" },
    right: { left: "calc(100% + 8px)", top: "50%", transform: "translateY(-50%)" },
  };
  return (
    <span
      style={{ position: "relative", display: "inline-flex", ...style }}
      onMouseEnter={() => setShow(true)}
      onMouseLeave={() => setShow(false)}
      {...rest}
    >
      {children}
      {show && (
        <span
          role="tooltip"
          style={{
            position: "absolute",
            ...pos[side],
            zIndex: 50,
            whiteSpace: "nowrap",
            padding: "6px 10px",
            background: "var(--ink-900)",
            color: "#fff",
            fontFamily: "var(--font-ui)",
            fontWeight: "var(--weight-medium)",
            fontSize: "var(--text-xs)",
            borderRadius: "var(--radius-xs)",
            boxShadow: "var(--shadow-md)",
            pointerEvents: "none",
          }}
        >
          {label}
        </span>
      )}
    </span>
  );
}
