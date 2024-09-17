import { useEffect, useState } from "react";
import { Form, useLoaderData } from "react-router-dom";
import { getUserDetails } from "./UserProfilePage";
import axios from "axios";
import ErrorPage from "../pages/ErrorPage";
import Button from '../components/Button';
import styles from '../styles/activitydetails.module.css';

export default function ActivityDetails() {
  const response = useLoaderData();
  const [userDetails, setUserDetails] = useState({});
  const [useError, setUseError] = useState(false);
  const [startsAt, setStartsAt] = useState(null);


  useEffect(() => {
	if (!response.error) {
	  const data = response.data;
	  getStartsAt(activity.starts_at, setStartsAt);
	  (async () => {
		  try {
			const res = await getUserDetails(data);
			setUserDetails(res.data);
		  } catch (error) {
			setUseError(true);
			console.log(error);
			setUserDetails(error)
		  }
	  })();
	}
  }, [response]);

  if (response.error) {
	return <ErrorPage error={response.data} />;
  }
  if (!userDetails) {
	return <p>Loading...</p>;
  }
  if (userDetails.error){
	return <ErrorPage error={userDetails.data} />;
  }
  const activity = response.data
  return (
	<>
		<div className={styles.heading}>
			<div className={styles.detailsImg}>
			</div>
			<div className={styles.titleBox}>
				<h2>{activity.title}</h2>
				<p className={styles.description}>
					{userDetails?.description ||
					`This ${activity.type} has no
					description`}
				</p>
				<div className={styles.userInfo}>
					<h4> Created By: </h4>
					<span>
					{! useError
						? `${userDetails.first_name}
								${userDetails?.last_name ?? ""}`
						: "❗️ We couldn't load this user's info"}
					</span>
					<span className={styles.userImg}>
						<img src="#" alt="" />
					</span>
				</div>
			</div>
		</div>
		<div className={styles.meta}>
			{ activity.status !== "live" ?
				<span className={styles.countDownBox}>
					Starts in:&nbsp;
					<span className={styles.countDown}>
						{getStartsAt(activity.starts_at)}
					</span>
				</span>
				:
				<></>
			}
			<Form method="post">
				<button type="button">Join</button>
			</Form>
		</div>
</>
);}

export async function loader({ params }) {
  try {
	const res = await axios.get(
	  `http://localhost:8082/api/v1/activities/${params.activityId}`,
	);
	return { error: false, data: res.data };
  } catch (error) {
	return { error: true, data: error };
  }
}

function getStartsAt(datestr, setter){
	const diff = new Date(datestr) - Date.now();
	const res = {
		seconds: Math.floor(diff / 1000),
		minutes: Math.floor(diff / (60000)),
		hours: Math.floor(diff / (60000 * 60)),
		days: Math.floor(diff / (60000 * 60 * 24)),
		weeks: Math.floor(diff / (3600000 * 24 * 7)),
		months: Math.floor(diff / (3600000 * 168 * 4)),
		years: Math.floor(diff / ( 3600000 * 8064))
	}

	return res.years > 0 ? `${res.years} years` :
			res.months > 0 ? `${res.months} months` :
			res.weeks > 0 ? `${res.weeks} weeks` :
			res.days > 0 ? `${res.days} days` :
			res.hours > 0 ? `${res.hours} hours` :
			res.minutes > 0 ? `${res.minutes} minutes` :
			res.seconds > 0 ? `${res.seconds} seconds` :
			"error";
}