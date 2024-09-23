/* Defines a  container structural component */
import '../styles/wrapper.css';

export default function Wrapper({clist=[], children}){
	let classes = `wrapper ${clist.join(" ")}`;
	return (<div className={classes}>{children}</div>);
}