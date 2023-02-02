import Severity from "@defined/severity";

interface AlertProps {
  openAlert: boolean;
  severity: Severity;
  message: string;
}

export default AlertProps;
