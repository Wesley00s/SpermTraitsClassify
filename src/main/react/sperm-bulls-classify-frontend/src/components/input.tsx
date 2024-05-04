import { Input } from "@chakra-ui/react"
import "./input.css";
import { UseFormRegister } from "react-hook-form";


interface InputProps {
    name: string;
    label: string;
    placeholder: string;
    register: UseFormRegister<any>;
    required?: boolean;
    error?: string;
}


export default function Inputs({ name, label, placeholder, register, required, error } : InputProps) {
    var type: string
    if (name == "hora") {
        type = "time"
    } else {
        type = "number"
    }
    
    return (
      <div className="input-container">
        <label className="label" htmlFor={name}>
          {label}
        </label>
  
        <Input
          type={type}
          variant="filled"
          placeholder={placeholder}
          {...register(name, { required })}
          />
        
        {error && <p className="error">{error}</p>}

        </div>
    );
  }





// interface InputProps {
//     name: string,
//     value: string,
//     onChange: ChangeEventHandler<HTMLInputElement>
//     label: string
//     placeholder: string
// }



//   export default function Inputs({ name, value, onChange, label, placeholder } : InputProps){
//     return (
//         <div className='input-container'>
//         <label className='label'>{label}</label>

//             <Input variant='filled'
//             placeholder={placeholder}
//             name={name}
//             value={value} 
//             onChange={onChange}
//         />
//         </div>
//     )
// }