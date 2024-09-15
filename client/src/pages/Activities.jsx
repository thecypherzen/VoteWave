/* Defines the Activities Route */

import { useLoaderData } from 'react-router-dom';
import axios from 'axios';

export default function Activities(){
	const activities = useLoaderData();

	return (
		<>
			<section>
				<h1>Activities</h1>
				<div id="activities">
					{activities?.error ?
					<div>
						<h3>We got an error</h3>
						<p><strong>{activities.error.response.statusText}: </strong>{activities.error.message}</p>
					</div> :
					<p><b>Status:&nbsp;</b>{activities.data.status}</p>
					}
				</div>
			</section>
		</>
	);
}

export async function loader(){
	try {
		const res = await axios.get("http://localhost:8082/api/v1/status");
		return res;
	} catch (err) {
		console.log(err);
		return {error: err};
	}
}