import Button from '../components/Button';
import "../styles/notfoundpage.css";

export default function NotFound(){
	return(
	<>
	<div id="content">
		<h1>We couldn't find that.</h1>
		<p>For now let's take you back home.</p>
		<Button clist={["btn", "btn-secondary"]}
			text={"Return home"} href="/" />
	</div>
	</>
	);
}