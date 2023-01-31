import React from "react";
import { Container } from "@mui/material";
import NavigationBar from "@components/NavigationBar";

interface PageLayoutProps {
  children?: JSX.Element | JSX.Element[] | string | string[];
}

const PageLayout: React.FC = (props: PageLayoutProps) => {
  return (
    <Container maxWidth="xl">
      <NavigationBar />
      {props.children}
    </Container>
  );
};

export default PageLayout;
