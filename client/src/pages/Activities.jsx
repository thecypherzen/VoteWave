/* Defines the Activities Route */

import { Outlet, useLoaderData } from 'react-router-dom';
import axios from 'axios';
import ActivitiesList from '../components/ActivitiesList';
import ErrorPage from './ErrorPage';
import Grid from "../components/Grid";
import NavBar from '../components/NavBar';
import Wrapper from "../components/Wrapper";
import "../styles/activities.css";
import "../styles/grid.css";

export default function Activities(){
	const response = useLoaderData();

	if (response.error){
		return(<ErrorPage error={response.data}
		/>)
	}
	const activities = response.data;
	return (
		<>
			<NavBar />
			<section id="activities">
				<div className="heading">
					<h1>Activities</h1>
					<p>Feel free to request to participate in any activity you like. They're public!</p>
				</div>
				<Wrapper>
					<Grid>
						<ActivitiesList activities={activities}/>
						<aside id="details">
							<Outlet/>
						</aside>
					</Grid>
				</Wrapper>
			</section>
		</>
	);
}

export async function loader(){
	try {
		const res = await axios.get("http://0:8082/api/v1/activities");
		return {error: false, data: res.data};
	} catch (err) {
		return {error: true, data: err};
	}
}