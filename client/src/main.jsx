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
import CallBack from './pages/CallBack';
import ErrorPage from './pages/ErrorPage';
import Landing from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import NotFound from './pages/NotFoundPage';
import OnBoardingPage from './pages/OnBoardingPage';
import UserDashboard from './pages/UserDashboard';

// loaders and actions
import { loader as activitiesLoader } from './pages/Activities';
import { loader as detailsLoader } from './pages/ActivityDetails';
import { loader as callbackLoader } from './pages/CallBack';
import { loader as onboardingLoader } from './pages/OnBoardingPage';
import { loader as userDashboardLoader } from './pages/UserDashboard';
import { loader as navBarUserLoader } from './components/PageNav';


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
		errorElement: <ErrorPage />,
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
	},
	{
		path: "/login",
		element: <LoginPage />,
		errorElement: <ErrorPage />
	},
	{
		path: "/login/verify",
		element: <CallBack />,
		errorElement: <ErrorPage />,
		loader: callbackLoader
	},
	{
		path: "/users/onboarding",
		element: <OnBoardingPage />,
		loader: onboardingLoader,
		errorElement: <ErrorPage />
	},
	{
		path: "/users/:userId/dashboard",
		element: <UserDashboard />,
		errorElement: <ErrorPage />,
		loader: userDashboardLoader
	}
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={ router }/>
  </React.StrictMode>,
);
