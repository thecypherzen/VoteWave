import React from 'react'
import ReactDOM  from 'react-dom/client'
import {
	createBrowserRouter,
	RouterProvider
} from 'react-router-dom'

import './styles/index.css'

// pages
import Activities from './pages/Activities';
import ActivityDetails from './pages/ActivityDetails';
import ActivitiesIndex from './pages/ActivitiesIndex';
import Landing from './pages/LandingPage';
import NotFound from './pages/NotFoundPage';

// loaders
import { loader as activitiesLoader } from './pages/Activities';
import { loader as detailsLoader } from './pages/ActivityDetails';

// router
const router = createBrowserRouter([
	{
		path: "/",
		element: <Landing />,
		errorElement: <NotFound />,
	},
	{
		path: "/activities/",
		element: <Activities />,
		loader: activitiesLoader,
		errorElement: <NotFound />,
		children: [
			{
				index: true,
				element: <ActivitiesIndex />
			},
			{
				path: "/activities/:activityId",
				element: <ActivityDetails />,
				loader: detailsLoader,
			}
		]
	}
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={ router }/>
  </React.StrictMode>,
);
