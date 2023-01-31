import { Suspense } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { StyledEngineProvider } from "@mui/material/styles";
import { CircularProgress, CssBaseline } from "@mui/material";
import Routing from "./routing";

function App() {
  return (
    <Suspense fallback={<CircularProgress />}>
      <BrowserRouter>
        <Routes>
          {Routing.map((route) => {
            const Component = route.component;
            return (
              <Route
                caseSensitive
                path={route.path}
                key={route.path}
                element={
                  <StyledEngineProvider injectFirst>
                    <CssBaseline />
                    <Component />
                  </StyledEngineProvider>
                }
              />
            );
          })}
        </Routes>
      </BrowserRouter>
    </Suspense>
  );
}

export default App;
