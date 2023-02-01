import { Button } from "@mui/material";
import { Download as DownloadIcon } from "@mui/icons-material";
import useDownloadFile from "@hooks/DownloadFile";

interface DownloadFileButtonProps {
  fileOutput: File | undefined;
}

type DownloadFileButtonComponent = ({}: DownloadFileButtonProps) => JSX.Element;

const DownloadFileButton: DownloadFileButtonComponent = (
  props: DownloadFileButtonProps
) => {
  const { ref, name, url, download } = useDownloadFile({
    fileOutput: props.fileOutput,
  });

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={<DownloadIcon />}
      onClick={download}
    >
      <a href={url} download={name} ref={ref} hidden />
      Download
    </Button>
  );
};

export default DownloadFileButton;
