/* Defines the Activities Route */

import { Outlet, useLoaderData, useNavigate
 } from 'react-router-dom';
import axios from 'axios';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import { faHouse } from '@fortawesome/free-solid-svg-icons';
import ActivitiesList from '../components/ActivitiesList';
import ErrorPage from './ErrorPage';
import Wrapper from "../components/Wrapper";
import styles from "../styles/activities.module.css";

export default function Activities(){
	const response = useLoaderData();
	const navigate = useNavigate();

	if (response.error){
		return(<ErrorPage context={response.data.message}
		/>)
	}
	const activities = response.data;
	return (
		<>
			<section className={styles.activities}>
				<div className={styles.heading}>
					<Wrapper>
						<span onMouseMove={e => showToolTip(e)}
						onMouseLeave={() => {
							document.getElementById("tooltip").
							style.display = "none";
						}}
						onClick={() => navigate("/")}
						className={styles.pageNav}>
							<FontAwesomeIcon icon={faHouse} />
							<span id="tooltip" className={styles.tooltip}>
								Home</span>
						</span>
						<h1>Activities</h1>
						<p>Feel free to request to participate in any activity you like. They're public!</p>
					</Wrapper>
				</div>
				<Wrapper>
					<div className={styles.grid}>
						<ActivitiesList activities={activities}/>
						<aside className={styles.details}>
							<Outlet/>
						</aside>
					</div>
				</Wrapper>
			</section>
		</>
	);
}

function showToolTip(e){
	const {clientX: x, clientY: y} = e;
	const tooltip = document.getElementById("tooltip");
	tooltip.style.display = "inline-flex";
	tooltip.style.left = `${x-85}px`;
	tooltip.style.top = `${y-60}px`;
}

export async function loader(){
	try {
		const res = await axios.get("http://0:8082/api/v1/activities");
		return {error: false, data: res.data};
	} catch (err) {
		return {error: true, data: err};
	}
}