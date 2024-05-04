package org.wesley.sperm.traits.classify.controller.dto

import org.wesley.sperm.traits.classify.model.Data

data class ReceiveDataDTO(
    val idade: Float,
    val peso: Float,
    val ec: Float,
    val ce: Float,
    val temp_retal: Float,
    val temp_amb: Float,
    val umidade: Float,
    val mov_flanco: Float,
    val hora: String,
    val turbilhao: Float,
    val mot_moveis: Float,
    val vigor: Float,
    val volume: Float,
    val zptz_106: Float,
    val zptz_totais: Float,
    val def_mai: Float,
    val def_mai_percent: Float,
    val def_men: Float,
    val def_men_percent: Float,
    val normais: Float,
    val normais_percent: Float
) {
    fun to(): Data {
        val data = Data()
        data.idade = idade
        data.peso = peso
        data.ec = ec
        data.ce = ce
        data.temp_retal = temp_retal
        data.temp_amb = temp_amb
        data.umidade = umidade
        data.mov_flanco = mov_flanco
        data.hora = hora
        data.turbilhao = turbilhao
        data.mot_moveis = mot_moveis
        data.vigor = vigor
        data.volume = volume
        data.zptz_106 = zptz_106
        data.zptz_totais= zptz_totais
        data.def_men = def_men
        data.def_men_percent = def_men_percent
        data.def_mai = def_mai
        data.def_mai_percent = def_mai_percent
        data.normais = normais
        data.normais_percent = normais_percent
        return data
    }

}
