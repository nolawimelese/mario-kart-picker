import { useEffect, useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import "./App.css";
import { Splash } from "./Splash";
import { Home } from "./Home";
import { fetchTracks } from "./api/tracks";
import { fetchHealth } from "./api/health";

function App() {
  const [view, setView] = useState<"splash" | "home">("splash");

  const { isPending, isSuccess, isError } = useQuery({
    queryKey: ["tracks"],
    queryFn: fetchTracks,
  });

  const healthCheck = useMutation({
    mutationFn: fetchHealth,
    onSuccess: () => setView("home"),
  });

  useEffect(() => {
    if (isSuccess && view === "splash") setView("home");
  }, [isSuccess, view]);

  return view === "splash" ? (
    <Splash
      loading={isPending}
      error={isError}
      checking={healthCheck.isPending}
      checkError={healthCheck.isError}
      onStart={() => healthCheck.mutate()}
    />
  ) : (
    <Home />
  );
}

export default App;
