import { useNavigate } from 'react-router-dom';
import Button from '../components/Button';
import styles from '../styles/errorpage.module.css';

export default function ErrorPage(data){
	const navigate = useNavigate();
	return (
	<div className={styles.errorContent}>
		<h1> Ouch!</h1>
		<p className={styles.errorMessage}>{data?.error?.message ?? "We encountered an error."}</p>
		{
			data?.error?.code ?
			<p><span>code: {data.error.code} </span> {
				console.log(data)
			}</p> :
			""
		}
		<div className={styles.btnBox}>
			<Button clickHandler={()=> {navigate("/")}}
					clist={["btn", "btn-dark"]}
					text="Return home"/>
		</div>
	</div>
	);
}