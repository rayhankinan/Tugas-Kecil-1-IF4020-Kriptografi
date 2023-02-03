import React from "react";
import { Box, TextField } from "@mui/material";

interface ResultDisplayTextProps {
  displayText: string | undefined;
  placeholder: string;
  isSeparated: boolean;
}

const ResultDisplayText: React.FC<ResultDisplayTextProps> = ({
  displayText,
  placeholder,
  isSeparated,
}: ResultDisplayTextProps) => {
  const processText = () => {
    if (!displayText) return;

    return isSeparated ? displayText.replace(/(.{5})/g, "$1 ") : displayText;
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        multiline
        fullWidth
        placeholder={placeholder}
        rows={10}
        value={processText()}
        variant="standard"
        InputProps={{
          readOnly: true,
        }}
      />
    </Box>
  );
};

export default ResultDisplayText;
