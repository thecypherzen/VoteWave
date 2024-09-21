import { useNavigate, useRouteError } from 'react-router-dom';
import Button from '../components/Button';
import styles from '../styles/errorpage.module.css';

export default function ErrorPage({context}){
	const navigate = useNavigate();
	const error = useRouteError();

	console.log("react error: ", error);
	return (
	<div className={styles.errorContent}>
		<h1> Ouch! We encountered an error.</h1>
		<h3 className={styles.runner}>
			These details may help...</h3>
		<div className={styles.errorDetails}>
			<p className={styles.errorMessage}>
				{error.message}
			</p>
			<hr />
			<p><strong>More context: </strong>
				{context}
			</p>
		</div>

		<div className={styles.btnBox}>
			<Button clickHandler={()=> {navigate("/")}}
					clist={["btn", "btn-dark"]}
					text="Return home"/>
		</div>
	</div>
	);
}