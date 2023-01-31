import React from "react";
import { useNavigate } from "react-router-dom";
import {
  AppBar,
  Box,
  Drawer,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";
import {
  Menu as MenuIcon,
  EnhancedEncryption as EnhancedEncryptionIcon,
} from "@mui/icons-material";

interface PageLink {
  name: string;
  url: string;
}

const NavigationBar: React.FC = () => {
  const [drawerOpened, setDrawerOpened] = React.useState(false);
  const navigate = useNavigate();

  const toggleDrawer = () => {
    setDrawerOpened(!drawerOpened);
  };

  const pageLinks: PageLink[] = [
    {
      name: "Affine",
      url: "/affine",
    },
    {
      name: "Auto Key Vigenere",
      url: "/auto-key-vigenere",
    },
    {
      name: "Enigma",
      url: "/enigma",
    },
    {
      name: "Extended Vigenere",
      url: "/extended-vigenere",
    },
    {
      name: "Hill",
      url: "/hill",
    },
    {
      name: "Playfair",
      url: "/playfair",
    },
    {
      name: "Vigenere",
      url: "/vigenere",
    },
  ];

  const generateList = (pageLinks: PageLink[]) => {
    return (
      <List>
        {pageLinks.map((pageLink) => (
          <ListItem key={pageLink.name} disablePadding>
            <ListItemButton onClick={() => navigate(pageLink.url)}>
              <ListItemIcon>
                <EnhancedEncryptionIcon />
              </ListItemIcon>
              <ListItemText primary={pageLink.name} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    );
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={toggleDrawer}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Tugas Kecil 1 IF4020 Kriptografi
          </Typography>
          <Drawer anchor="left" open={drawerOpened} onClose={toggleDrawer}>
            {generateList(pageLinks)}
          </Drawer>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default NavigationBar;
