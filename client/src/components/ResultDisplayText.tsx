import React from "react";
import { Box, TextField } from "@mui/material";

interface ResultDisplayTextProps {
  displayText: string | undefined;
  isSeparated: boolean;
}

const ResultDisplayText: React.FC<ResultDisplayTextProps> = (
  props: ResultDisplayTextProps
) => {
  const processText = () => {
    if (!props.displayText) return;

    return props.isSeparated
      ? props.displayText.replace(/(.{5})/g, "$1 ")
      : props.displayText;
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        multiline
        fullWidth
        rows={10}
        defaultValue={processText()}
        variant="standard"
        InputProps={{
          readOnly: true,
        }}
      />
    </Box>
  );
};

export default ResultDisplayText;
