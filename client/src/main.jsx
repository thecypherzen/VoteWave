import React from 'react'
import ReactDOM  from 'react-dom/client'
import {
	createBrowserRouter,
	RouterProvider
} from 'react-router-dom'

import './styles/index.css'

// pages
import Activities from './pages/Activities';
import Landing from './pages/LandingPage';
import NotFound from './pages/NotFoundPage.jsx';

// loaders
import { loader as activitiesLoader } from './pages/Activities';

// router
const router = createBrowserRouter([
	{
		path: "/",
		element: <Landing />,
		errorElement: <NotFound />,
	},
	{
		path: "/activities/live",
		element: <Activities />,
		loader: activitiesLoader,
		errorElement: <NotFound />
	}
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={ router }/>
  </React.StrictMode>,
);
