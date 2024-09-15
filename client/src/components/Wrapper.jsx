/* Defines a  container structural component */
import '../styles/wrapper.css';

export default function Wrapper({children}){
	return (<div className="wrapper">{children}</div>)
}