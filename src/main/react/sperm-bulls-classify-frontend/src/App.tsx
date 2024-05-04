import { useState } from 'react'
import './App.css'
import Inputs from './components/input'
import { Button, Stack } from '@chakra-ui/react'
import { useDataMutation } from './hooks/useDataMutation'
import { useForm } from 'react-hook-form'

const App = () => {
  const { mutate }= useDataMutation()
  const [responseMessage, setResponseMessage] = useState<string>('');
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [isSending, setIsSending] = useState<boolean>(false); // Utilizando o estado do React


  const onSubmit = async (data: any) => {
    try {
      setIsSending(true); // Ativa a animação de loading
      const response = await mutate(data);
      console.log(response);
      setResponseMessage(response);
    } catch (error) {
      console.error("Erro na requisição:", error);
      setResponseMessage('Erro ao processar a requisição.');
    } finally {
      setIsSending(false); // Desativa a animação de loading após receber a resposta
    }
  };

  return (
    
    <div className="container">
      <h1 className='title'>Avaliar aptidão reprodutiva de touros Guzerá</h1>

      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="inputs">
          <Inputs
            label="Idade"
            name="idade"
            placeholder="0.0"
            register={register}
            required
            error={errors.idade && "Idade obrigatória*"}
          />

          <Inputs
            label="Peso"
            name="peso"
            placeholder="0.0"
            register={register}
            required
            error={errors.peso && "Peso obrigatório*"}
          />

          <Inputs
            label="EC"
            name="ec"
            placeholder="0.0"
            register={register}
            required
            error={errors.ec && "EC obrigatório*"}
          />

          <Inputs
            label="CE"
            name="ce"
            placeholder="0.0"
            register={register}
            required
            error={errors.ce && "CE obrigatório*"}
          />

          <Inputs
            label="Temp. ret."
            name="temp_retal"
            placeholder="0.0"
            register={register}
            required
            error={errors.temp_retal && "Temp. Ret. obrigatória*"}
          />

          <Inputs
            label="Temp. amb."
            name="temp_amb"
            placeholder="0.0"
            register={register}
            required
            error={errors.temp_amb && "Temp. Amb. obrigatória*"}
          />

          <Inputs
            label="Umidade"
            name="umidade"
            placeholder="0.0"
            register={register}
            required
            error={errors.umidade && "Umidade obrigatória*"}
          />

          <Inputs
            label="Mov. flanco"
            name="mov_flanco"
            placeholder="0.0"
            register={register}
            required
            error={errors.mov_flanco && "Mov. Flanco obrigatório*"}
          />

          <Inputs
            label="Hora da coleta"
            name="hora"
            placeholder="00:00"
            register={register}
            required
            error={errors.hora && "Hora obrigatória*"}
          />


          <Inputs
            label="Turbilão"
            name="turbilhao"
            placeholder="0.0"
            register={register}
            required
            error={errors.idade && "Turbulão obrigatório*"}
          />

          <Inputs
            label="Mot. Moveis"
            name="mot_moveis"
            placeholder="0.0"
            register={register}
            required
            error={errors.mot_moveis && "Mot. Moveis obrigatória*"}
          />

          <Inputs
            label="Vigor"
            name="vigor"
            placeholder="0.0"
            register={register}
            required
            error={errors.vigor && "Vigor obrigatório*"}
          />

          <Inputs
            label="Volume"
            name="volume"
            placeholder="0.0"
            register={register}
            required
            error={errors.volume && "Volume obrigatório*"}
          />

          <Inputs
            label="Zptz 10⁶"
            name="zptz_106"
            placeholder="0.0"
            register={register}
            required
            error={errors.zptz_106 && "Zptz 10⁶ obrigatório*"}
          />

          <Inputs
            label="Zptz. Totais"
            name="zptz_totais"
            placeholder="0.0"
            register={register}
            required
            error={errors.zptz_totais && "Zptz. Totais obrigatório*"}
          />

          <Inputs
            label="Def. Mai."
            name="def_mai"
            placeholder="0.0"
            register={register}
            required
            error={errors.def_mai && "Def. Mai. obrigatório*"}
          />

          <Inputs
            label="Def. Mai.%"
            name="def_mai_percent"
            placeholder="0.0"
            register={register}
            required
            error={errors.def_mai_percent && "Def. Mai.% obrigatório*"}
          />

          <Inputs
            label="Def. Men."
            name="def_men"
            placeholder="0.0"
            register={register}
            required
            error={errors.def_men && "Def. Men. obrigatório*"}
          />

          <Inputs
            label="Def.Men.%"
            name="def_men_percent"
            placeholder="0.0"
            register={register}
            required
            error={errors.def_men_percent && "Def. Men.% obrigatório*"}
          />

          <Inputs
            label="Normais"
            name="normais"
            placeholder="0.0"
            register={register}
            required
            error={errors.normais && "Normais obrigatório*"}
          />

          <Inputs
            label="Normais%"
            name="normais_percent"
            placeholder="0.0"
            register={register}
            required
            error={errors.normais_percent && "Normais% obrigatório*"}

          />
          <div className="box-response">
         {/* Renderização condicional do botão */}
         {isSending ? ( // Se estiver enviando, exibe o botão de "Enviando dados"
            <Stack direction='row' margin={5}>
              <Button
                isLoading
                loadingText='Enviando dados'
                colorScheme='teal'
                variant='outline'
              >
                Enviando dados
              </Button>
            </Stack>
          ) : ( // Caso contrário, exibe o botão "Enviar dados"
            <Button
              type="submit"
              size='md'
              height='48px'
              width='auto'
              border='2px'
              borderColor='green.500'
              margin={5}
            >
              Enviar dados
            </Button>
          )}
        </div>
        </div>
          
          <div className="response-box">
            <h2 className='waiting'>Aguardando resposta...</h2>
              <div className="response-container">
                  <p className="response">
                    {responseMessage}
                  </p>
              </div>
          </div>
      </form>
    </div>
  )
}

export default App


