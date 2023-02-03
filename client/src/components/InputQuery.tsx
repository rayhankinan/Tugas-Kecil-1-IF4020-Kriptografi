import React from "react";
import { Box, TextField } from "@mui/material";

interface InputQueryProps {
  parameter: string;
  placeholder: string;
  query: Record<string, string>;
  setQuery: React.Dispatch<React.SetStateAction<Record<string, string>>>;
}

const InputQuery: React.FC<InputQueryProps> = ({
  parameter,
  placeholder,
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
        placeholder={placeholder}
        variant="standard"
        value={query?.[parameter]}
        onChange={handleChange}
      />
    </Box>
  );
};

export default InputQuery;
