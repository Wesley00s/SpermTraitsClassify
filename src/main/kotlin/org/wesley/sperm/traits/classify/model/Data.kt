package org.wesley.sperm.traits.classify.model

import jakarta.persistence.*
import java.time.LocalDateTime

@Entity
class Data {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    var id: Long = 0

    var dateTime: LocalDateTime = LocalDateTime.now()

    @Column(nullable = false)
    var idade: Float = 0f

    @Column(nullable = false)
    var peso: Float = 0f

    @Column(nullable = false)
    var ec: Float = 0f

    @Column(nullable = false)
    var ce: Float = 0f

    @Column(nullable = false)
    var temp_retal: Float = 0f

    @Column(nullable = false)
    var temp_amb: Float = 0f

    @Column(nullable = false)
    var umidade: Float = 0f

    @Column(nullable = false)
    var mov_flanco: Float = 0f

    @Column(nullable = false)
    var hora: String = ""

    @Column(nullable = false)
    var turbilhao: Float = 0f

    @Column(nullable = false)
    var mot_moveis: Float = 0f

    @Column(nullable = false)
    var vigor: Float = 0f

    @Column(nullable = false)
    var volume: Float = 0f

    @Column(nullable = false)
    var zptz_106: Float = 0f

    @Column(nullable = false)
    var zptz_totais: Float = 0f

    @Column(nullable = false)
    var def_mai: Float = 0f

    @Column(nullable = false)
    var def_mai_percent: Float = 0f

    @Column(nullable = false)
    var def_men: Float = 0f

    @Column(nullable = false)
    var def_men_percent: Float = 0f

    @Column(nullable = false)
    var normais: Float = 0f

    @Column(nullable = false)
    var normais_percent: Float = 0f
}