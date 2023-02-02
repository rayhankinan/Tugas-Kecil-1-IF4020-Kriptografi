import React from "react";
import { Box, TextField } from "@mui/material";

interface InputQueryProps {
  parameter: string;
  query: Record<string, string> | undefined;
  setQuery: React.Dispatch<
    React.SetStateAction<Record<string, string> | undefined>
  >;
}
