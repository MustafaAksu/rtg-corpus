# RER Phase A r6 — bağımsız alıcı incelemesi

**Tarih:** 19 Ekim 2026  
**Statü:** NONCANONICAL alıcı inceleme makbuzu; RER adoption/freeze/release değildir.  
**Karar:** **ACCEPT SCOPED — kaynak edinimi / mekanik bütünlük**; `A6-G8-01` kaynak-satırı sınıflandırması sonraki metadata revizyonunda düzeltilmeli. Hiçbir bilimsel kayıt bu kararla kabul edilmez.

## 1. Bağımsızca çalıştırılan kontroller

- Gelen ZIP `RER_PHASEA_R6_PACKAGE_20261019.zip`: SHA-256 `909a4beb6da40c7ae3ddf3fa339d6efb0ab85281ab5dbc9078201294b6ffff0c`.
- Paket `SHA256SUMS.txt`: **59/59** giriş tam hash eşleşmesi (ZIP'te dizinlerle birlikte 65 member).
- Çıkarım `RER_phaseA_r6/`; `python -I build_phaseA.py`, `python -I check_phaseA.py --tamper` her ikisi de başarılı. **22/22 pozitif kapı PASS; 22/22 kurcalama kontrolü hedeflenen kapıda reddedildi.** Betikler temiz çıkarılmış kopyada çalıştırıldı. Günlükler bu inceleme klasöründedir.
- RER r4.6 Markdown SHA-256: `2fa878ffa32c0d4d725f53f17b86b9a43d5161f16a7adce9686cb374063a4772`, r5 ile **bayt-aynı**.
- Phase A r5 ve r6 `out/RER_REGISTRY_v0_2_r4_6_PHASEA.json`: yalnız `schema` farklı; `records`, `gap_entries`, `counts`, `source_table`, `legacy_v0_1_snapshot` ve diğer bilimsel içerik aynıdır.
- r5/r6 `out/BLOCKED_SOURCE_REGISTER.json`: yalnız `schema` ve `byte_availability_gap` değişmiş. ER-2B engel nesneleri birebir korunmuş.
- Kaynak matrisinde **89** satır (76 import + 13 gap); **35** değişen satır. Değişen satırlarda kimlik/konum/alıntı hash'leri korunmuştur.

## 2. İthal kaynak ediniminin sonucu

R6'ya eklenen 14 `sources_available/` dosyası için gerçek kaynak baytlarının SHA-256'sı hem `inputs/source_custody_r6.json` beyanıyla hem aynı anahtarın RER import satırlarında basılı hash'iyle eşleştirildi: **14/14 PASS**. Bu, dosyaların elde bulunan nüshalarının özdeşliğini doğrular; **orijinal container ZIP'lerin SHA-256 ve üye yolunun doğrudan karşılaştırılması değildir**. `A22`, kayıtlı container adının varlığını kontrol eder; container baytlarını açıp yeniden hash'lemez. Mevcut oturumda anılan ayrı kaynak ZIP'lerin orijinalleri bu denetim için erişilebilir değildi. `container_sha256`, `member`, `supplied_by` zinciri bu noktada hazırlayanın beyanıdır.

Güncel matrix:

| Durum | Sayı |
|---|---:|
| `VERIFIED` | 30 |
| `OWNER_REPORTED` | 4 |
| `HISTORICAL` | 48 |
| `BLOCKED` | 7 |

Authentication: `BYTE_VERIFIED_HERE` **58**; `RECEIVER_BYTE_VERIFIED` **6**; `HASH_PRINTED_UNVERIFIED` **24**; `UNAUTHENTICATED_NO_HASH` **1**. Bu 58 farklı kaynak anlamına gelmez; tekrarlı import satırları aynı dosyayı kullanabilir. RECOG v0.3.20 hash doğrulaması, kendi belgesindeki **freeze-candidate** statüsünü adoption'a yükseltmez.

## 3. A6-G8-01 — ER01 satırının gereğinden geniş bloklanması

**Bulguyu doğrudan kaynaktan doğruladım.** `sources_available/ER01__RTG_ER2B_CONSOLIDATED_STUDY_v0_1.md` dosyasının §5, `ER2B-C15`, satır 452–482'si pasif koordinat taşıması (kapanış `Σ_e H(z_e)=0` biçiminde taşınır) ile yeni chart içinde yeniden `Σ_e z_e=0` kurulmasını farklı modeller olarak ayırıyor. Kaynağın basılı SHA-256'sı `267c6f37e70220dac02b22b605ef77b8faea009d90db764139887c115cd1fb44` ve gerçek dosya SHA-256'sıyla aynı.

`RER-G8` ilk `Reference:` satırının kanıtı **bu v0.1 kaynak metnidir**. V0.2 C19–C20 kaynak paketinin bulunmaması, v0.1 C15'in kaynaktan okunmasını engellemiyor. Buna rağmen r6 kaynak matrisi, `catalog_sources.json` içindeki **anahtar-düzeyi** `ER01.rule = BLOCKED` yüzünden `RER-G8 / GAP_REFERENCE / n=0 / ER01` satırını `status: BLOCKED` gösteriyor. Yeni A22 kapısı **bütün** ER01 satırlarının BLOCKED olmasını zorlayarak bu fazla geniş sınıflamayı pekiştiriyor.

**Alıcı disposition:** G8/0 için önerilen doğru satır kapsamı `authentication=BYTE_VERIFIED_HERE`, `bytes_status=BYTE_VERIFIED_MATCH`, `status=HISTORICAL` (v0.1 noncanonical eski kaynak), `currency=SNAPSHOT_RECHECK_IN_PHASE_B`, `gap_reference_review=PENDING_PER_REFERENCE_AUDIT`. `ER2B-C15`'in doğrulanmış metni ayrıca RRF v0.8.3 §0.3'teki model/pasif-rechart ayrımıyla uyumludur, ancak bu bilimsel adoption değildir. `RER-ER2B-T6D`, `RER-ER2B-CARRIER` ve onların ER01 import satırları `BLOCKED` kalır; v0.2 birincil paket yoktur. ER01 için kayıt-düzeyi/gap-düzeyi sınıflama ayrılmalı; A22'nin negatif kontrolü bir **bilimsel ER-2B kaydını** yanlışlıkla açmayı reddetmeyi sürdürmelidir. RER Markdown'ı değişmemelidir.

Bu bulgu **22/22 mekanik kapı çıktısını inkâr etmez**; mevcut kapının kendi kuralının bu bir satır için fazla geniş olduğunu gösterir. G8/0'ın source status düzeltilmesi tam matris-kullanımında gereklidir; r6'nın kaynak edinimi ve byte-identity delta kabulünü engellemez.

## 4. Phase B GEN-C01–C09 hazırlığının sınırı

`RER-GEN-C01–C09` için matrisin verdiği doğrudan eldeki/eksik importlar:

| Kayıt | Byte-matched kaynak anahtarları | Eksik import anahtarları |
|---|---|---|
| GEN-C01–C03 | `GENMODEL` | `HARM` |
| GEN-C04 | `ANGLE` | `HARM`, `ANGLE_DATA` |
| GEN-C05 | `RANK` | `RANKDATA` |
| GEN-C06 | `F3` | — |
| GEN-C07 | `F3`, `GENMODEL` | — |
| GEN-C08 | `REACH` | — |
| GEN-C09 | `AGE`, `JET` | — |

C01–C05'in kaynak-paket erişimi **tam değildir**; mevcut kanıtlarla scoped okuma yapılabilir ama eksik kaynakları doldurmadan tam yeniden üretim/kanıt kapsaması iddia edilemez. C06–C09 için listelenen importların byte availability'si tamamdır; bu, matematiksel reproof veya bilimsel kabul anlamına gelmez.

## 5. Değişmeyen sınırlar ve sonraki iş

- RER r4.6 DRAFT; 20 kayıt adoption `PENDING`; iki ER-2B kaydı `BLOCKED_SOURCE_UNVERIFIED`.
- 13 gap referansının `gap_reference_review` alanı `PENDING_PER_REFERENCE_AUDIT` kalır; RRF editör Q1–Q8 yanıtı ayrı bir teslimdir.
- `G2NOTE04` orijinal dosyası/hashi bulunmadığından `CARRIER_IDENTIFICATION_PENDING`.
- Phase B'nin GEN-C01–C09 okuma notlarına başlanabilir. Eksik `HARM`, `ANGLE_DATA`, `RANKDATA` kaynaklarını ilgili kayıt notlarında ayrı görünür bağımlılık yapın. Hazırlayanın yazarı olduğu iki Triadic involüsyon kaydı bağımsız alıcıya ayrılmıştır.
- Kaynak dosyaları, JSON sicili veya proje kaynakları bu incelemeyle değiştirilmedi; yeni adoption, freeze, yayın, fiziksel gerçekleştirme veya bilimsel grade yükseltmesi yoktur.

**Kanıt katmanları:** `[SESSION]` doğrudan SHA/test/JSON farkı; `[OWNER: RRF v0.8.3 §0.3]` temsil-safety ilkesi; `[NONCANONICAL SOURCE: ER-2B v0.1 §5 C15]` mevcut ayrım. Orijinal container provenance bağımsız doğrulanmadı.
