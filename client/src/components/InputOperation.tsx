import React from "react";
import {
  FormControl,
  MenuItem,
  Select,
  SelectChangeEvent,
} from "@mui/material";
import Operation from "@defined-types/operation";

interface InputOperationProps {
  operation: Operation;
  setOperation: React.Dispatch<React.SetStateAction<Operation>>;
}

const InputOperation: React.FC<InputOperationProps> = ({
  operation,
  setOperation,
}: InputOperationProps) => {
  const [open, setOpen] = React.useState<boolean>(false);

  const handleChange = (event: SelectChangeEvent<Operation>) => {
    const { value } = event.target;

    setOperation(value as Operation);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <FormControl>
      <Select
        open={open}
        onOpen={handleOpen}
        onClose={handleClose}
        value={operation}
        onChange={handleChange}
      >
        <MenuItem value="encrypt-file">Encrypt</MenuItem>
        <MenuItem value="decrypt-file">Decrypt</MenuItem>
      </Select>
    </FormControl>
  );
};

export default InputOperation;
