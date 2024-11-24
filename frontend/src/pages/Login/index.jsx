import './Login.css';
import TField from '../../Components/TField';
import TFieldSenha from '../../Components/TFieldSenha';
import BtnEntrar from '../../Components/BtnEntrar';
import LoginIcon from '@mui/icons-material/Login';
import BtnVoltar from '../../Components/BtnVoltar';

function Login() {
  return (<>
    <BtnVoltar pagina={'/'} />
    <main className='container text-center tela_login'>
      <div className='h-100 d-flex flex-column align-items-center justify-content-around'>
        <div className="img_container_login" data-titulo='Fresh Photo'>
          <img src='assets/logo_login.png' alt='pedaço de melancia com Fresh Photo escrito em baixo' id='img_logo' />
        </div>
        <form className='h-50 d-flex flex-column justify-content-around'>
          <TField id_campo={'t_field_login'} texto='Usuário ou email' tamanho='small' />
          <TFieldSenha tamanho='small' />
          <a href='#'><p className='text-start ms-2'>Esqueceu sua senha?</p></a>
          <BtnEntrar texto={'login'} componente={<LoginIcon />} id_entrada={'btn_login'} />
        </form>
      </div>
    </main>
  </>
  );
}

export default Login;
