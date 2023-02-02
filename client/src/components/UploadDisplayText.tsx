import React from "react";
import { Box, TextField } from "@mui/material";

interface UploadDisplayTextProps {
  displayText: string | undefined;
  setDisplayText: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const UploadDisplayText: React.FC<UploadDisplayTextProps> = ({
  displayText,
  setDisplayText,
}: UploadDisplayTextProps) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target;

    setDisplayText(value);
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        multiline
        fullWidth
        rows={10}
        variant="standard"
        value={displayText}
        onChange={handleChange}
      />
    </Box>
  );
};

export default UploadDisplayText;
