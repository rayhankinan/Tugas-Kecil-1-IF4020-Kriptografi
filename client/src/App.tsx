import { Suspense } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { StyledEngineProvider } from "@mui/material/styles";
import { CircularProgress, CssBaseline } from "@mui/material";
import Routing from "./routing";

const App = () => {
  return (
    <StyledEngineProvider injectFirst>
      <CssBaseline />
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
                  element={<Component />}
                />
              );
            })}
          </Routes>
        </BrowserRouter>
      </Suspense>
    </StyledEngineProvider>
  );
};

export default App;
