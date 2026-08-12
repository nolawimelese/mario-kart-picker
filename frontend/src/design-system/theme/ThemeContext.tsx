import React, { createContext, useContext, useEffect, useState } from "react";

export type Theme = "light" | "dark";

interface ThemeContextValue {
  darkMode: boolean;
  setDarkMode: (next: boolean) => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

const STORAGE_KEY = "mkpicker:theme";

/** Reads the saved theme; falls back to light if unset or if storage is unavailable. */
function readStoredTheme(): Theme {
  try {
    return localStorage.getItem(STORAGE_KEY) === "dark" ? "dark" : "light";
  } catch {
    return "light";
  }
}

/** Applies the active theme to <html data-theme> so tokens/colors.css can react to it. */
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(readStoredTheme);

  useEffect(() => {
    if (theme === "dark") {
      document.documentElement.dataset.theme = "dark";
    } else {
      delete document.documentElement.dataset.theme;
    }
    // Storage can throw in private-browsing modes — the theme still applies for this session.
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch {
      /* preference just won't persist */
    }
  }, [theme]);

  const value: ThemeContextValue = {
    darkMode: theme === "dark",
    setDarkMode: (next) => setTheme(next ? "dark" : "light"),
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components -- hook is colocated with its provider
export function useTheme(): ThemeContextValue {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within a ThemeProvider");
  return ctx;
}
