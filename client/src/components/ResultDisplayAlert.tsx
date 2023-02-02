import React from "react";
import { Alert, Snackbar } from "@mui/material";
import AlertProps from "@interface/alert-props";

interface ResultDisplayAlertProps {
  alertProps: AlertProps;
  setAlertProps: React.Dispatch<React.SetStateAction<AlertProps>>;
}

const ResultDisplayAlert: React.FC<ResultDisplayAlertProps> = ({
  alertProps,
  setAlertProps,
}: ResultDisplayAlertProps) => {
  const handleClose = () => {
    const newAlertProps = { ...alertProps };
    newAlertProps.openAlert = false;
    setAlertProps(newAlertProps);
  };

  return (
    <Snackbar
      open={alertProps.openAlert}
      autoHideDuration={1000}
      onClose={handleClose}
    >
      <Alert
        onClose={handleClose}
        severity={alertProps.severity}
        sx={{ width: "100%" }}
      >
        {alertProps.message}
      </Alert>
    </Snackbar>
  );
};

export default ResultDisplayAlert;
