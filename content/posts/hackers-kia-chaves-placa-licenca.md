---
title: "Hackers Obtêm Chaves Para Qualquer Kia Apenas Com Uma Placa de Licença"
description: "Uma nova falha na segurança dos veículos Kia permite que hackers tenham acesso a praticamente todos os modelos produzidos após 2013. Entenda o que aconteceu e as implicações para a cibersegurança automotiva."
tags: ['Kia', 'Segurança Veicular', 'Cibersegurança', 'Carros Elétricos']
thumbnail: "https://cdn.motor1.com/images/mgl/eoKBGA/s3/kia-kiatool-security-vulnerability.jpg"
slug: "hackers-kia-chaves-placa-licenca"
author: "Rob Stumpf"
date: "28/09/2024 06:01"
---

## Introdução

A Kia não está passando por um bom momento nos últimos anos em relação à segurança veicular. Desde os chamados "Kia Boys", que alertaram sobre 5 milhões de veículos sem imobilizadores, até dispositivos pequenos que facilitam o furto de carros, nunca foi tão fácil para ladrões agirem em veículos coreanos.

## O Ataque Recente

Uma nova prova de conceito, que se tornou conhecida simplesmente como "Kia Hack", representa um dos ataques mais significativos a veículos Kia que já vimos. Embora este problema já tenha sido corrigido, é vital discutir o que ocorreu, pois isso reflete o futuro da cibersegurança automotiva.

### O Pesquisador de Segurança

Esse ataque foi revelado por **Curry**, um pesquisador de segurança renomado. Ao contrário de usar um martelo para quebrar janelas, ele utilizou sequências de teclas para alcançar o mesmo resultado: o acesso a praticamente todos os veículos Kia produzidos após 2013.

## Como Funciona o Ataque

O método envolve o serviço Kia Connect, uma plataforma que permite aos proprietários desbloquear seus carros ou ativar recursos como o aquecimento remotamente. Com um pouco de pesquisa, Curry conseguiu explorar a falha na API da Kia, que gerava um token de sessão para usuários autenticados. Esse token permitia o envio de comandos para os servidores da Kia e, consequentemente, o controle do carro.

### A Falha na API

Curry tirou proveito de uma vulnerabilidade na API do KDealer, usada para registrar novos veículos. Ele conseguiu acessar o Número de Identificação do Veículo (VIN) através de uma placa de licença, similar a obter uma cotação de um carro usado, e usar essa informação para simular um registro falso, ganhando acesso remoto a quase todos os modelos Kia produzidos na última década.

## Implicações

### Ameaças à Segurança

Essa vulnerabilidade apresenta uma enorme ameaça aos veículos. O acesso remoto não apenas facilita o roubo, mas também compromete a segurança do proprietário, que pode ter suas informações pessoais, como nome, telefone e até mesmo a localização do veículo, expostas a galhos mal-intencionados.

#### Questões de Privacidade

Os atacantes podem monitorar informações e criar um sofisticado plano para roubar veículos, utilizando virtualmente qualquer informação acessível, como a localização do carro, e até ativando câmeras remotamente.

## Resposta da Kia

Felizmente, a Kia já corrigiu a falha e confirmou que a vulnerabilidade não foi explorada em ataques reais. Curry divulgou eticamente a falha à montadora em junho, e após Correções serem implementadas em agosto, ele fez a divulgação pública de suas descobertas.

## Conclusão

Esta situação é um lembrete claro sobre as vulnerabilidades da tecnologia em carros conectados. À medida que a internet se torna uma parte essencial dos veículos, as falhas de segurança podem levar a consequências reais e sérias. Esta discussão sobre a cibersegurança na indústria automotiva é fundamental para garantir a segurança e a privacidade dos usuários.

*Este post foi baseado no artigo de Rob Stumpf do site [InsideEVs](https://insideevs.com/news/735373/kia-hack-cyber-security-researcher/).*