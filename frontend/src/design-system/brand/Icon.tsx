import React from "react";

export type IconName =
  | "search" | "x" | "check" | "chevron-down" | "chevron-up" | "chevron-right"
  | "chevron-left" | "arrow-right" | "plus" | "minus" | "star" | "zap" | "heart"
  | "trophy" | "flag" | "shuffle" | "dice" | "gauge" | "timer" | "route"
  | "sliders" | "user" | "info" | "alert" | "check-circle" | "lock" | "play"
  | "settings" | "medal" | "sparkles" | "map";

export interface IconProps extends Omit<React.SVGProps<SVGSVGElement>, "color"> {
  /** Which glyph to render. */
  name: IconName;
  /** Pixel size (width = height). Default 20. */
  size?: number;
  /** Stroke width. Default 2. */
  strokeWidth?: number;
  /** Stroke color. Default currentColor. */
  color?: string;
}

/* MK Picker icon set.
   Outline icons in the Lucide style (2px round stroke) — the codebase shipped
   no product icon set, so these are drawn from the open-source Lucide library
   (ISC licensed) to give the brand a consistent friendly line look.
   Add new glyphs to PATHS using Lucide's 24x24 path data. */

const PATHS = {
  search: ["circle:11,11,8", "M21 21l-4.3-4.3"],
  x: ["M18 6 6 18", "M6 6l12 12"],
  check: ["M20 6 9 17l-5-5"],
  "chevron-down": ["m6 9 6 6 6-6"],
  "chevron-up": ["m18 15-6-6-6 6"],
  "chevron-right": ["m9 18 6-6-6-6"],
  "chevron-left": ["m15 18-6-6 6-6"],
  "arrow-right": ["M5 12h14", "m12 5 7 7-7 7"],
  plus: ["M5 12h14", "M12 5v14"],
  minus: ["M5 12h14"],
  star: ["M12 2.5l2.9 5.9 6.6 1-4.8 4.6 1.1 6.5-5.8-3-5.8 3 1.1-6.5L2.5 9.4l6.6-1z"],
  zap: ["M13 2 3 14h9l-1 8 10-12h-9l1-8z"],
  heart: ["M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"],
  trophy: ["M6 9H4.5a2.5 2.5 0 0 1 0-5H6", "M18 9h1.5a2.5 2.5 0 0 0 0-5H18", "M4 22h16", "M10 14.7V17c0 .6-.5 1-1 1.2C7.9 18.8 7 20.2 7 22", "M14 14.7V17c0 .6.5 1 1 1.2 1.1.5 2 2 2 4.8", "M18 2H6v7a6 6 0 0 0 12 0V2Z"],
  flag: ["M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z", "M4 22v-7"],
  shuffle: ["M16 3h5v5", "M4 20 21 3", "M21 16v5h-5", "M15 15l6 6", "M4 4l5 5"],
  dice: ["rect:3,3,18,18,3", "circle:8.5,8.5,1", "circle:15.5,8.5,1", "circle:15.5,15.5,1", "circle:8.5,15.5,1", "circle:12,12,1"],
  gauge: ["m12 14 4-4", "M3.34 19a10 10 0 1 1 17.32 0"],
  timer: ["M10 2h4", "M12 14l3-3", "circle:12,14,8"],
  route: ["circle:6,19,3", "M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15", "circle:18,5,3"],
  sliders: ["M4 21v-7", "M4 10V3", "M12 21v-9", "M12 8V3", "M20 21v-5", "M20 12V3", "M1 14h6", "M9 8h6", "M17 16h6"],
  user: ["circle:12,7,4", "M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"],
  info: ["circle:12,12,10", "M12 16v-4", "M12 8h.01"],
  alert: ["m21.7 18-8-14a2 2 0 0 0-3.4 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3Z", "M12 9v4", "M12 17h.01"],
  "check-circle": ["circle:12,12,10", "m9 12 2 2 4-4"],
  lock: ["rect:3,11,18,11,2", "M7 11V7a5 5 0 0 1 10 0v4"],
  play: ["m6 3 14 9-14 9V3z"],
  settings: ["M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z", "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1Z"],
  medal: ["M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15", "M11 12 5.12 2.2", "M13 12l5.88-9.8", "M8 7h8", "circle:12,17,5", "M12 18v-2h-.5"],
  sparkles: ["M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z", "M5 18l.7 1.8L7.5 20.5l-1.8.7L5 23l-.7-1.8L2.5 20.5l1.8-.7z"],
  map: ["M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z", "M9 4v14", "M15 6v14"],
};

export function Icon({ name, size = 20, strokeWidth = 2, color = "currentColor", style, ...rest }: IconProps) {
  const segs = PATHS[name];
  if (!segs) return null;
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      style={{ display: "block", flexShrink: 0, ...style }}
      {...rest}
    >
      {segs.map((s, i) => {
        if (s.startsWith("circle:")) {
          const [cx, cy, r] = s.slice(7).split(",");
          return <circle key={i} cx={cx} cy={cy} r={r} />;
        }
        if (s.startsWith("rect:")) {
          const [x, y, w, h, rx] = s.slice(5).split(",");
          return <rect key={i} x={x} y={y} width={w} height={h} rx={rx} />;
        }
        return <path key={i} d={s} />;
      })}
    </svg>
  );
}
