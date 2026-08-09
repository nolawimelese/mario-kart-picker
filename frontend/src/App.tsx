import { useEffect, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import "./App.css";
import { Splash } from "./Splash";
import { Home } from "./Home";
import { fetchTracks } from "./api/tracks";

function App() {
  const [view, setView] = useState<"splash" | "home">("splash");

  const { isPending, isSuccess, isError } = useQuery({
    queryKey: ["tracks"],
    queryFn: fetchTracks,
  });

  useEffect(() => {
    if (isSuccess && view === "splash") setView("home");
  }, [isSuccess, view]);

  return view === "splash" ? (
    <Splash
      loading={isPending}
      error={isError}
      onStart={() => setView("home")}
    />
  ) : (
    <Home />
  );
}

export default App;
