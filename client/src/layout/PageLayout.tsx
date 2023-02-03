import React from "react";
import { Container } from "@mui/material";
import NavigationBar from "@components/NavigationBar";

interface PageLayoutProps {
  children?: JSX.Element | JSX.Element[] | string | string[];
}

const PageLayout: React.FC<PageLayoutProps> = ({
  children,
}: PageLayoutProps) => {
  return (
    <React.Fragment>
      <NavigationBar />
      <Container maxWidth="lg" sx={{ py: 2 }}>
        {children}
      </Container>
    </React.Fragment>
  );
};

export default PageLayout;
