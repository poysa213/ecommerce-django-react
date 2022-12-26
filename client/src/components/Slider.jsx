import {  ArrowLeftOutlined, ArrowRightOutlined } from '@mui/icons-material'
import React from 'react'
import styled from 'styled-components'


const Container = styled.div`
    width: 100%;
    height: 100vh;
    display: flex;
    background-color: #14213d;
    position: relative;
`

const Arrow = styled.div`
  width: 50px;
  height: 50px;
  background: whitesmoke;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 0;
  bottom: 0;
  left: ${props=> props.direction === 'left' && "10px"};
  right: ${props=> props.direction === 'right' && "10px"};
  margin: auto;
  cursor: pointer;
  opacity: 0.5;
`
const Wrapper = styled.div`
height: 100%;

`

const Slide = styled.div`
  display: flex;
  align-items: center;
  height: 100vh;
  width: 100vw;
`

const ImgContainer = styled.div`
  flex: 1;
  height: 100%;
`

const Image = styled.image`
  height: 80%;
`
const InfoContainer = styled.div`
  flex: 1;
  padding: 50px;
`
const Title = styled.h1``
const Desc = styled.p``
const Btn = styled.button``

const Slider = () => {
  return (
   <Container>
    <Arrow direction='left'>
        <ArrowLeftOutlined />
    </Arrow>
    <Wrapper>
      <Slide>
      <ImgContainer><Image src="https://toppng.com/uploads/preview/2d-cut-out-people-casual-v-6-cadrender-store-standing-people-11562922951vo0k3crbgz.pnghttps://toppng.com/uploads/preview/2d-cut-out-people-casual-v-6-cadrender-store-standing-people-11562922951vo0k3crbgz.png" /></ImgContainer>
      <ImgContainer><Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNONeiTQtadkyLAlSf0wku7zYAa9nlAbu2y2yOxXVBPA&s" /></ImgContainer>
    <InfoContainer>
      <Title>Hhh</Title>
      <Desc></Desc>
      <Btn></Btn>
    </InfoContainer>
    </Slide>
    </Wrapper>
    <Arrow direction='right'>
    <ArrowRightOutlined />
    </Arrow>
   </Container>
  )
}

export default Slider