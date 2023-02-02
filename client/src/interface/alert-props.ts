import Severity from "@defined-types/severity";

interface AlertProps {
  openAlert: boolean;
  severity: Severity;
  message: string;
}

export default AlertProps;
