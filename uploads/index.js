import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router";

import { routes } from './routes/routes';

const root = ReactDOM.createRoot(document.getElementById('main'));

const router = createBrowserRouter(routes);
root.render(
  <React.StrictMode>
   <RouterProvider router={router}></RouterProvider>
  </React.StrictMode>
);

