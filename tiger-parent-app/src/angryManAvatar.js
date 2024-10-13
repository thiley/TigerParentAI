import React from 'react';
import angryParent from './assets/angryParent.png';

const angryParentAvatar = () =>{
    console.log("Custom Bot Avatar Rendered");
    return(
        <div>
            <img 
            src={angryParent}
            alt="angry parent avatar"
            style={{ width: '40px', height: '40px', borderRadius: '50%' }}
            />
        </div>
    );
};

export default angryParentAvatar;