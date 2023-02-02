import React from "react";
import { Box, TextField } from "@mui/material";

interface InputQueryProps {
  parameter: string;
  query: Record<string, string> | undefined;
  setQuery: React.Dispatch<
    React.SetStateAction<Record<string, string> | undefined>
  >;
}

const InputQuery: React.FC<InputQueryProps> = ({
  parameter,
  query,
  setQuery,
}: InputQueryProps) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target;

    const newQuery = { ...query };
    newQuery[parameter] = value;
    setQuery(newQuery);
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        fullWidth
        variant="standard"
        value={query?.[parameter]}
        onChange={handleChange}
      />
    </Box>
  );
};

export default InputQuery;
